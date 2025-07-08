"""
Punto de entrada principal para el servidor MCP de generación de imágenes con DALL-E2.
"""
import os
import logging
import uvicorn
from dotenv import load_dotenv
from mcp_server.app import init_server

# Cargar variables de entorno
load_dotenv()

# Configuración de logging
logging.basicConfig(
    level=os.getenv("MCP_SERVER_LOG_LEVEL", "info").upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Iniciando servidor MCP para generación de imágenes")
        host = os.getenv("MCP_SERVER_HOST", "0.0.0.0")
        port = int(os.getenv("MCP_SERVER_PORT", "8000"))
        
        # Inicializar el servidor MCP
        server = init_server()
        
        uvicorn.run(
            server,
            host=host,
            port=port,
            reload=os.getenv("ENVIRONMENT", "production").lower() == "development",
        )
    except Exception as e:
        logger.error(f"Error al iniciar el servidor: {e}")
        raise
