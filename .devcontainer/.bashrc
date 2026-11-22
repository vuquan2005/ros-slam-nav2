# Interactive terminal configuration.
[[ $- == *i* ]] || return

# Load ble.sh before the theme and attach after the remaining shell setup.
if [ -f "$HOME/.local/share/blesh/ble.sh" ]; then
    source "$HOME/.local/share/blesh/ble.sh" --noattach
fi

export OSH="$HOME/.oh-my-bash"
OSH_THEME="robbyrussell"
plugins=(git sudo colored-man-pages)
if [ -f "$OSH/oh-my-bash.sh" ]; then
    source "$OSH/oh-my-bash.sh"
else
    PS1='\u@\h:\w\$ '
fi

# Set loopback transport IP for Ignition / Gazebo Fortress
export IGN_IP=127.0.0.1
export GZ_IP=127.0.0.1

# Load the ROS underlay before any workspace overlay.
if [ -f "/opt/ros/${ROS_DISTRO:-humble}/setup.bash" ]; then
    source "/opt/ros/${ROS_DISTRO:-humble}/setup.bash"
fi
if [ -f /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash ]; then
    source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
fi

if [ -f /usr/share/colcon_cd/function/colcon_cd.sh ]; then
    source /usr/share/colcon_cd/function/colcon_cd.sh
    export _colcon_cd_root="${ROS_DIF_WORKSPACE:-/workspaces/ros-dif}"
fi

if [ -f install/setup.bash ]; then
    source install/setup.bash
elif [ -f "${ROS_DIF_WORKSPACE:-/workspaces/ros-dif}/install/setup.bash" ]; then
    source "${ROS_DIF_WORKSPACE:-/workspaces/ros-dif}/install/setup.bash"
fi

if [ -d "$HOME/.local/bin" ]; then
    case ":$PATH:" in
        *":$HOME/.local/bin:"*) ;;
        *) export PATH="$HOME/.local/bin:$PATH" ;;
    esac
fi
if [ -d /commandhistory ] && [ -w /commandhistory ]; then
    export HISTFILE=/commandhistory/.bash_history
else
    export HISTFILE="$HOME/.bash_history"
fi
export HISTSIZE=50000
export HISTFILESIZE=50000
export HISTCONTROL=ignoreboth:erasedups
shopt -s histappend
PROMPT_COMMAND+=('history -a; history -n')

if [[ ${BLE_VERSION-} ]]; then
    ble-attach
fi
