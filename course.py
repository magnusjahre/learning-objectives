
import pandas as pd
from objective import LearningObjective

class Course:

    def __init__(self, code, learning_objective_file):
        self.code = code
        self.datafile = pd.read_excel(learning_objective_file)

        self.knowledge = self.build_learning_objectives("K")
        self.skills = self.build_learning_objectives("S")
        self.general_competence = self.build_learning_objectives("G")

    def build_learning_objectives(self, lo_type):
        los = []

        type_df = self.datafile.loc[self.datafile["Type (K,S,G)"] == lo_type]
        for i, row in type_df.iterrows():
            los.append(LearningObjective(row))

        return los

    def __str__(self):
        return self.code
