# Museum Simulation – Gazebo Harmonic

## Beschreibung

Diese Simulation enthält eine Museumswelt mit einem großen Raum für die autonome Navigation eines TurtleBot3.

Das Museum wurde in Sweet Home 3D erstellt, in Blender bearbeitet und als COLLADA-Modell (`museum.dae`) für Gazebo exportiert.

## Voraussetzungen

- Ubuntu 24.04
- Gazebo Harmonic
- ROS 2 Jazzy für die spätere Roboterintegration

## Museum starten

Im Projektordner folgenden Befehl ausführen: 
(Ins Projektordner Terminal kommt man wenn man im Ordner Rechtsklick auf den Hintergrund macht und "in Terminal öffnen" anklickt falls dus nicht wusstest)

./scripts/start_museum.sh

Das Skript setzt den benötigten Gazebo-Modellpfad und startet die Museumswelt.

## Startposition des Roboters

Vorgesehene Startkoordinaten:

- X: 3.5933 m
- Y: -1.7835 m
- Yaw: 0.0 rad

Die Z-Koordinate muss passend zum verwendeten TurtleBot3-Modell bestimmt werden.

Die Werte sind zusätzlich in `config/spawn_positions.yaml` dokumentiert.

Die Startposition wurde noch nicht mit dem tatsächlichen Roboter getestet.

## Projektstruktur

- `worlds/museum_world.sdf` – Gazebo-Welt
- `models/museum/model.sdf` – Museumsmodell und Kollisionsgeometrie
- `models/museum/model.config` – Modellbeschreibung
- `models/museum/meshes/` – 3D-Modell und Texturen
- `config/spawn_positions.yaml` – Roboter-Startkoordinaten
- `scripts/start_museum.sh` – Startskript

## Bisherige Tests

- Die Museumswelt wird erfolgreich in Gazebo geladen.
- Das Startskript funktioniert.
- Die Größe wurde visuell mit einem 1-Meter-Würfel verglichen.
- Bodenkollisionen und weitere ausgewählte Kollisionen wurden erfolgreich getestet.

## Zuständigkeiten

Die Museumswelt wird als statische Simulationsumgebung bereitgestellt.

Die Integration des TurtleBot3, seiner Sensoren, der ROS-Gazebo-Bridge, SLAM und Nav2 erfolgt separat.

## Noch zu testen

- TurtleBot3 in der Museumswelt spawnen
- Tatsächliche Roboter-Startposition überprüfen
- LiDAR und Kamera testen
- Navigation mit SLAM und Nav2 testen
- Geeignete Positionen für Suchobjekte festlegen
