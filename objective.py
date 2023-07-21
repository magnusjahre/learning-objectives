
learning_objective_types = {"K": "Knowledge",
                            "S": "Skill",
                            "G": "General Competence"}


class LearningObjective:

    def __init__(self, data):
        self.acm = data["ACM Curriculum ID"]
        self.bloom = data["Bloom Level"]
        self.activities = data["Learning activities"]
        self.assessment = data["Assessed by"]
        self.type = data["Type (K,S,G)"]

        # TODO: This needs to be a parent ID for this to work
        self.level = data["Hierarchy ID"]

        self.objective_nor = data["Learning objective (Norwegian)"]
        self.objective_eng = data["Learning objective (English)"]
