# utils.py - Fonctions utilitaires pour le Projet Chimera
import time
import random

class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.status = "idle"

    def perform_action(self):
        self.status = "working"
        time.sleep(random.uniform(0.1, 1.0))
        self.status = "idle"
        return f"Agent {self.id} a terminé son action."

class Simulation:
    def __init__(self, num_agents):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.running = False

    def start(self):
        self.running = True
        print("Simulation démarrée.")

    def stop(self):
        self.running = False
        print("Simulation arrêtée.")
