# Image Generation MCP Server

Servidor MCP para capacidades de generación y edición de imágenes utilizando DALL-E2.

## Acerca del proyecto

Este proyecto implementa un servidor Model Context Protocol (MCP) que proporciona una interfaz unificada para la generación y edición de imágenes utilizando el modelo DALL-E2 de OpenAI.

## Documentación

- [PLANNIG.md](./PLANNIG.md) - RFC con el diseño técnico y arquitectura
- [TASK.md](./TASK.md) - Tareas de implementación organizadas por bloques

## Estado

🚧 **En Desarrollo** - Este proyecto se encuentra actualmente en implementación.

## Requisitos

- Python 3.10+
- Clave de API de OpenAI
- ModelContextProtocol Python SDK

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/yourusername/image-generation-mcp-server.git
   cd image-generation-mcp-server
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Edita el archivo .env y añade tu clave de API de OpenAI
   ```

## Ejecución

Para iniciar el servidor MCP:

```bash
python src/main.py
```

El servidor estará disponible en `http://localhost:8000` por defecto.

## Estructura del proyecto

```
.
├── src/
│   ├── main.py                     # Punto de entrada principal
│   ├── mcp_server/                 # Módulo del servidor MCP
│   │   ├── app.py                  # Definición de la aplicación FastAPI
│   │   ├── config.py               # Gestión de configuración
│   │   └── tools/                  # Herramientas MCP
│   └── services/                   # Servicios externos
│       └── openai_client.py        # Cliente para OpenAI
├── .env.example                    # Ejemplo de variables de entorno
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
```

## Herramientas disponibles

El servidor MCP expondrá las siguientes herramientas:

- **ImageGenerationTool**: Para generar imágenes a partir de un texto descriptivo.
- **ImageEditingTool**: Para editar imágenes existentes utilizando texto y una máscara opcional.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del repositorio
2. Crea una nueva rama para tu función o corrección
3. Envía un pull request

## Licencia

[MIT](LICENSE)
