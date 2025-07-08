"""
Cliente asíncrono para la API de OpenAI (DALL-E2).
"""
import logging
from typing import Dict, List, Optional, Any, Union
from openai import AsyncOpenAI
from ..mcp_server.config import config

# Configurar logger
logger = logging.getLogger(__name__)

class AsyncOpenAIClient:
    """
    Cliente asíncrono para la API de OpenAI con soporte para operaciones
    de generación y edición de imágenes usando DALL-E2.
    """
    
    def __init__(self):
        """
        Inicializa el cliente OpenAI con la configuración desde las variables de entorno.
        """
        self.api_key = config.OPENAI_API_KEY
        self.max_retries = config.OPENAI_MAX_RETRIES
        self.timeout = config.OPENAI_TIMEOUT_SECONDS
        
        # Configurar cliente OpenAI
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            timeout=self.timeout,
            max_retries=self.max_retries
        )
        
        logger.info("Cliente OpenAI inicializado")
    
    async def generate_images(
        self, 
        prompt: str, 
        n: int = 1, 
        size: str = "1024x1024",
        model: str = "dall-e-2"
    ) -> Dict[str, Any]:
        """
        Genera imágenes a partir de un prompt utilizando DALL-E2.
        
        Args:
            prompt: Texto descriptivo para la generación de imágenes.
            n: Número de imágenes a generar (1-10).
            size: Tamaño de las imágenes ("256x256", "512x512", "1024x1024").
            model: Modelo a utilizar ("dall-e-2").
            
        Returns:
            Dict[str, Any]: Respuesta de la API de OpenAI con las URLs de las imágenes generadas.
        """
        try:
            logger.info(f"Generando {n} imágenes con el prompt: {prompt[:50]}...")
            
            # Preparar parámetros para la API
            params = {
                "model": model,
                "prompt": prompt,
                "n": n,
                "size": size,
            }
            
            # Realizar la llamada a la API con reintentos
            for retry in range(self.max_retries + 1):
                try:
                    response = await self.client.images.generate(**params)
                    logger.info(f"Imágenes generadas exitosamente: {len(response.data)}")
                    return response
                except Exception as e:
                    if retry < self.max_retries:
                        import asyncio
                        wait_time = 2 ** retry  # Backoff exponencial
                        logger.warning(f"Intento {retry + 1} fallido. Reintentando en {wait_time}s. Error: {e}")
                        await asyncio.sleep(wait_time)
                    else:
                        raise
            
        except Exception as e:
            logger.error(f"Error al generar imágenes: {e}")
            raise
    
    async def edit_image(
        self,
        image_data: bytes,
        prompt: str,
        mask_data: Optional[bytes] = None,
        n: int = 1,
        size: str = "1024x1024",
        model: str = "dall-e-2"
    ) -> Dict[str, Any]:
        """
        Edita una imagen existente a partir de un prompt y una máscara opcional.
        
        Args:
            image_data: Datos binarios de la imagen a editar.
            prompt: Texto descriptivo para la edición de la imagen.
            mask_data: Datos binarios de la máscara (opcional).
            n: Número de imágenes a generar (1-10).
            size: Tamaño de las imágenes editadas.
            model: Modelo a utilizar.
            
        Returns:
            Dict[str, Any]: Respuesta de la API de OpenAI con las URLs de las imágenes editadas.
        """
        try:
            import io
            logger.info(f"Editando imagen con el prompt: {prompt[:50]}...")
            
            # Crear objetos de archivo a partir de los bytes
            image_file = io.BytesIO(image_data)
            image_file.name = "image.png"  # El nombre es requerido por la API
            
            # Preparar parámetros para la API
            params = {
                "model": model,
                "image": image_file,
                "prompt": prompt,
                "n": n,
                "size": size,
            }
            
            # Añadir máscara si está presente
            if mask_data:
                mask_file = io.BytesIO(mask_data)
                mask_file.name = "mask.png"
                params["mask"] = mask_file
            
            # Realizar la llamada a la API
            for retry in range(self.max_retries + 1):
                try:
                    response = await self.client.images.edit(**params)
                    logger.info(f"Imagen editada exitosamente: {len(response.data)} variaciones generadas")
                    return response
                except Exception as e:
                    if retry < self.max_retries:
                        wait_time = 2 ** retry  # Backoff exponencial
                        logger.warning(f"Intento {retry + 1} fallido. Reintentando en {wait_time}s. Error: {e}")
                        import asyncio
                        await asyncio.sleep(wait_time)
                    else:
                        raise
            
        except Exception as e:
            logger.error(f"Error al editar imagen: {e}")
            raise
