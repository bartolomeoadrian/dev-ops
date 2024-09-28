<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Logo-up.jpg" height="100px"/>
</p>

# Dev Ops

This project includes a Python API built with Flask that communicates with the Gemini API. Below are the steps to set up and run the API.

## Table of Contents

-   [Prerequisites](#prerequisites)
-   [Configuration](#configuration)
-   [Installation](#installation)

## Prerequisites

-   Docker

## Configuration

Create a `.env` file in the root directory of the project and add the following variables:

```env
PORT=5000

DEBUG=
SENTRY_DSN=
GITHUB_TOKEN=
```

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/bartolomeoadrian/dev-ops
    cd dev-ops
    ```

2. Run the docker-compose file:

    ```sh
    docker-compose up
    ```
