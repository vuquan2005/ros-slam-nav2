#!/usr/bin/env bash
set -eo pipefail

workspace_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source /etc/os-release

if [[ "${ID:-}" != ubuntu || "${VERSION_ID:-}" != 22.04 ]]; then
    printf 'Script yêu cầu Ubuntu 22.04 LTS. Hệ điều hành hiện tại: %s\n' "${PRETTY_NAME:-không xác định}" >&2
    exit 1
fi

if [[ "$EUID" == 0 ]]; then
    printf 'Chạy script bằng tài khoản có quyền sudo.\n' >&2
    exit 1
fi

if [[ ! -f "$workspace_dir/src/dif_bringup/package.xml" ]]; then
    printf 'Đặt script ở thư mục gốc của mã nguồn ROS DIF.\n' >&2
    exit 1
fi

cd "$workspace_dir"
sudo apt-get update
sudo apt-get install -y software-properties-common ca-certificates curl python3
sudo add-apt-repository -y universe

# Reuse a working ROS 2 APT source on machines that already have one.
if ! apt-cache show ros-humble-desktop >/dev/null 2>&1; then
    apt_source_dir="$(mktemp -d)"
    trap 'rm -f -- "$apt_source_dir/ros2-apt-source.deb"; rmdir -- "$apt_source_dir"' EXIT
    release_tag="$(
        curl -fsSL --retry 3 https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest |
            python3 -c 'import json, sys; print(json.load(sys.stdin)["tag_name"])'
    )"
    curl -fsSL --retry 3 \
        "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${release_tag}/ros2-apt-source_${release_tag}.jammy_all.deb" \
        -o "$apt_source_dir/ros2-apt-source.deb"
    sudo dpkg -i "$apt_source_dir/ros2-apt-source.deb"
    sudo apt-get update
fi

sudo apt-get install -y \
    build-essential cmake python3-colcon-common-extensions python3-rosdep python3-yaml \
    ros-humble-desktop ros-humble-ros-gz \
    libgl1-mesa-dri libegl1-mesa

if [[ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]]; then
    sudo rosdep init
fi

source /opt/ros/humble/setup.bash
rosdep update --rosdistro humble
rosdep install --from-paths src --ignore-src --rosdistro humble -y
colcon build --symlink-install --base-paths src

printf '\nCài đặt hoàn tất. Chạy mô phỏng từ thư mục dự án bằng các lệnh sau:\n'
printf 'source install/setup.bash\nros2 launch dif_bringup sim.launch.py\n'
