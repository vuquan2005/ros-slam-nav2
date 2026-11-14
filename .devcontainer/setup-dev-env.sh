#!/usr/bin/env bash
set -euo pipefail
workspace_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Install shell customizations in the container user account.
if [ ! -d "$HOME/.oh-my-bash" ]; then
    git clone --depth=1 https://github.com/ohmybash/oh-my-bash.git "$HOME/.oh-my-bash"
fi

ble_dir="$HOME/.local/share/blesh"
if [ ! -f "$ble_dir/ble.sh" ]; then
    ble_tmp_dir="$(mktemp -d)"
    trap 'rm -rf -- "$ble_tmp_dir"' EXIT
    curl --fail --location --retry 3 \
        https://github.com/akinomyoga/ble.sh/releases/download/nightly/ble-nightly.tar.xz \
        --output "$ble_tmp_dir/ble.tar.xz"
    tar -xJf "$ble_tmp_dir/ble.tar.xz" -C "$ble_tmp_dir"
    mkdir -p "$ble_dir"
    cp -a "$ble_tmp_dir/ble-nightly/." "$ble_dir/"
fi

cp "$workspace_dir/.devcontainer/.bashrc" "$HOME/.bashrc"

# A named volume keeps history across container rebuilds. Seed only once.
history_file="$HOME/.bash_history"
if [ -d /commandhistory ]; then
    sudo chown "$(id -u):$(id -g)" /commandhistory
    history_file=/commandhistory/.bash_history
    if [ -f "$history_file" ]; then
        sudo chown "$(id -u):$(id -g)" "$history_file"
    fi
fi
if [ ! -s "$history_file" ]; then
    if [ -s "$HOME/.bash_history" ] && [ "$history_file" != "$HOME/.bash_history" ]; then
        cp "$HOME/.bash_history" "$history_file"
    else
        cp "$workspace_dir/.devcontainer/history_seed.txt" "$history_file"
    fi
fi

# ROS setup scripts do not consistently support nounset.
set +u
source /opt/ros/humble/setup.bash
rosdep update --rosdistro humble
cd "$workspace_dir"
rosdep install --from-paths src --ignore-src --rosdistro humble -r -y
printf '\nROS DIF ready. Run: colcon build --symlink-install --base-paths src\n'
