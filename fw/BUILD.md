# ARCHITEKTUR — ECHTE STEUERUNG (kein App, kein pyparrot)
# Schritt 1: Clone
# git clone --depth 1 https://github.com/Parrot-Developers/arsdk_manifests.git
# Schritt 2: Build (Linux/Unix native)
# ./build.sh -p arsdk-native -t build-sample-JumpingSumoSample -j
# Schritt 3: Run
# ./out/arsdk-native/staging/native-wrapper.sh ./out/arsdk-native/staging/usr/bin/JumpingSumoSample
# Schritt 4: Verbinden via WiFi (JumpingSumo-b037841) und steuern
# Hinweis: Windows hat kein natives build.sh — braucht Linux-VM oder Build-Server
