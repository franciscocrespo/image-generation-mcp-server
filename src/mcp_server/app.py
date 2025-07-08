"""
Configuración principal del servidor MCP para generación de imágenes.
"""
import logging
from mcp.server.fastmcp import FastMCP
from mcp.transports.streamable_http import StreamableHTTPTransport
from .config import config

# Configurar logger
logger = logging.getLogger(__name__)

# Stateful server (maintains session state)
mcp = FastMCP("DALL-E2 Image Generation")

# Función para inicializar el servidor
def init_server():
    """
    Inicializa el servidor MCP y configura los componentes necesarios.
    Debe llamarse durante el arranque de la aplicación.
    """
    logger.info("Iniciando servidor MCP para generación de imágenes con DALL-E2")
    
    # Verificar configuración de OpenAI
    if not config.OPENAI_API_KEY:
        logger.warning("¡ADVERTENCIA! No se ha configurado OPENAI_API_KEY. El servidor no podrá conectarse a la API de OpenAI.")
    
    # En el Bloque 3 se registrarán aquí las herramientas MCP
    
    # Run server with streamable_http transport
    return mcp.run(transport="streamable-http")
