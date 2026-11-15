FROM osrf/ros:humble-desktop-jammy

ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=1000
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential cmake git sudo curl ca-certificates gawk xz-utils \
        python3-colcon-common-extensions python3-rosdep python3-yaml \
        ros-humble-ros-gz ros-humble-xacro \
        ros-humble-robot-state-publisher ros-humble-joint-state-publisher \
        ros-humble-teleop-twist-keyboard \
        ros-humble-joy ros-humble-teleop-twist-joy \
        ros-humble-slam-toolbox ros-humble-nav2-map-server \
        ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-twist-mux \
        libgl1-mesa-dri libegl1-mesa mesa-utils \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m -s /bin/bash ${USERNAME} \
    && usermod -aG dialout,video ${USERNAME} \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

RUN if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then rosdep init; fi
ENV USER=${USERNAME} \
    LOGNAME=${USERNAME}
USER ${USERNAME}
WORKDIR /workspaces/ros-dif
