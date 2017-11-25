# Instalación de Docker para Ubuntu

1. Es recomendable comprobar que tenemos Ubuntu actualizado:
  - Actualizar los repositorios:

          sudo apt-get update

  - Comparar las versiones instaladas con las disponibles y actualizar aquellas que estén obsoletas:

          sudo apt-get upgrade

1. Desinstalar Docker por si tenemos alguna versión antigua.

        sudo apt-get remove docker docker-engine docker.io

1. Instalar apt-transport-https y ca-certificates. Instale los paquetes para permitir a APT el uso de un repositorio a través de HTTPS

        sudo apt-get install \
            apt-transport-https \
            ca-certificates \
            curl \
            software-properties-common

1. Añadir clave oficial de Docker GPG:

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

1. Utilice el siguiente comando para configurar el repositorio Stable . Siempre necesitas el repositorio Stable , incluso si quieres instalar compilaciones desde repositorios edge o testing también. Para añadir los repositorios de edge o testing , añada la palabra edge o testing (o ambas) después de la palabra stable en los comandos siguientes.

        sudo add-apt-repository \
           "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
           $(lsb_release -cs) \
           stable"
Compruebe que la huella digital clave es: "9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88". Para ello busca utilizando los últimos 8 caracteres de la huella:

        sudo apt-key fingerprint 0EBFCD88
Con respuesta:

        pub   4096R/0EBFCD88 2017-02-22
              Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
        uid                  Docker Release (CE deb) <docker@docker.com>
        sub   4096R/F273FCD8 2017-02-22

1. Refrescamos la caché del gestor de paquetes en Ubuntu.

        sudo apt-get update
1. Instale la versión más reciente de Docker CE

        sudo apt-get install docker-ce

1. Para comprobar que se ha instalado correctamente ejecutamos **docker run**. Si nos devuele “Hello world” está todo instalado perfectamente.

        sudo docker run ubuntu /bin/echo 'Hello world'

### Basado en:
- https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#next-steps
