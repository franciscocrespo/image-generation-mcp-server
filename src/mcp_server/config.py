"""
Módulo para la gestión de configuración y secretos del servidor MCP.
"""
import os
from typing import Optional
from dotenv import load_dotenv
import logging

# Configurar logger
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

class Config:
    """Clase para gestionar la configuración del servidor MCP."""
    
    # OpenAI API Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MAX_RETRIES: int = int(os.getenv("OPENAI_MAX_RETRIES", "3"))
    OPENAI_TIMEOUT_SECONDS: int = int(os.getenv("OPENAI_TIMEOUT_SECONDS", "30"))
    
    # Server Configuration
    MCP_SERVER_HOST: str = os.getenv("MCP_SERVER_HOST", "0.0.0.0")
    MCP_SERVER_PORT: int = int(os.getenv("MCP_SERVER_PORT", "8000"))
    MCP_SERVER_LOG_LEVEL: str = os.getenv("MCP_SERVER_LOG_LEVEL", "info").upper()
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production").lower()
    
    @classmethod
    def validate_config(cls) -> bool:
        """
        Valida que todas las configuraciones requeridas estén presentes.
        
        Returns:
            bool: True si todas las configuraciones requeridas están presentes, False en caso contrario.
        """
        if not cls.OPENAI_API_KEY:
            logger.error("OPENAI_API_KEY no está configurada")
            return False
        
        logger.info("Configuración validada correctamente")
        return True
    
    @classmethod
    def get_proxy_settings(cls) -> dict:
        """
        Obtiene la configuración de proxy si está definida.
        
        Returns:
            dict: Diccionario con la configuración de proxy.
        """
        proxies = {}
        http_proxy = os.getenv("HTTP_PROXY")
        https_proxy = os.getenv("HTTPS_PROXY")
        
        if http_proxy:
            proxies["http"] = http_proxy
        
        if https_proxy:
            proxies["https"] = https_proxy
        
        return proxies


# Validar configuración al importar el módulo
config = Config()
if not config.validate_config():
    logger.warning("La configuración no es válida, algunas funcionalidades pueden no estar disponibles")
