#!/bin/bash
#SPDX-FileCopyrightText: 2023 Sho Yoshida
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 15 ros2 launch mypkg janken_pub_sub.launch.py / > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep 'rock'
