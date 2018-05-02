# so-exam2
# Parcial 2  
  
**Universidad Icesi**  
**Curso:** Sistemas Operativos  
**Estudiante:** Juan Camilo Villada Gamboa  
**Codigo:** A00320192  
**Correo:** jncvg17@hotmail.com  
  
 **Instalacion y configuración de Oh-My-Zsh y sus plugins**

 1. Se instala en Debian Zsh, paquete que es necesario para la instalación de Oh-My-Zshell tal y como indica en su pagina Robbie Russell. Se instala con el comando:

```
 sudo apt-get install zsh
```

2. Como parte de los prerrequisitos para la instalacion de Oh-My-Zsh, tambien se encuentra la instalacion de Curl o Wget, en este caso, se instalara Curl en el sistema operativo Debian con el siguiente comando:

```
 sudo apt-get install curl
```

3. Una vez instalado curl y asumiendo que tenemos git instalado en el sistema, podemos proceder a la instalacion de Oh-My-Zsh a traves del siguiente comando:

```
 sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```


**Configuración de Github Token y shortcuts zsh**

4. Despues de instalado Oh-My-Zsh clonamos el repositorio so-exam2 y configuramos el repositorio con un token de Github para realizar modificaciones en el. El token se debe obtener del perfil personal de Github. El comando para realizar la configuracion una vez obtenido es:

```
git config remote.origin.url "https://tokengoeshere@github.com/JnCV17/so-exam2.git"
```

5. Realizamos algunos cambios al README.md para probar los shortcuts gaa (git add --all), gcmsg (git commit -m), ggp (git push origin <actual-branch>)


**Instalacion de Plugins para Oh-My-Zsh**

6. Una vez instalado Oh-My-Zsh procedemos a instalar uno de sus plugins que sugiere el autocompletado de comandos previamente invocados por el usuario usando el siguiente comando:

```
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

7. Se adiciona el plugin a la lista de plugins activos usando:

```
vi ~/.zshrc
plugins=(git vi-mode zsh-autosuggestions)

source ~/.zshrc
```


8. Para cambiar el color del resaltado de la sugeriencia del plugin a amarillo se modifica el archivo zsh-autosuggestions.zsh:  
```
vi $ZSH_CUSTOM/jvillada.zsh
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=yellow"
source ~/.zshrc
```

**Instalación TMUX**
1. Se instala tmux usando el siguiente comando:

```
sudo apt-get install tmux
```

2. Una vez instalado tmux, se cambiara su configuración para facilitar el uso de atajos de teclado, en este caso se cambiaran comandos como **ctrl+a = ctrl+b**. De igual forma se activara vi-mode y la selección, usando el siguiente comando:

```
vi ~/.tmux.conf
```

En el archivo tmux.conf añadimos lo siguiente:

```
# use C-a, since it's on the home row and easier to hit than C-b
set-option -g prefix C-a
unbind-key C-a
bind-key C-a send-prefix
set -g base-index 1

# Easy config reload
bind-key R source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."

# vi is good
setw -g mode-keys vi

# Setup 'v' to begin selection as in Vim
bind-key -Tcopy-mode-vi v send -X begin-selection
```

3. Usando tmux se crea una nueva sesion llamada so-exam2 y se divide en 4 cuadrantes para cada nos de los procesos requeridos:   
*- 4 cuadrantes tmux*  
*- Salida del comando top*  
*- Salida de la ejecución del script de python courses.py*  
*- Peticiones por medio de curl a cada endpoint. Salida formateada con jq*  
*- Salida de la ejecución de telnet towel.blinkenlights.nl*  


