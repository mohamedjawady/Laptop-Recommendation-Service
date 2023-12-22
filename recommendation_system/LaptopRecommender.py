from experta import KnowledgeEngine, Rule
from .Price import Price
from .Usage import Usage



class LaptopRecommender(KnowledgeEngine):

    # the recommendation type
    recommendation = "default"


    @Rule(Usage('gaming and design') & Price('High'))
    def recommend_gaming_design_high_price(self):
        LaptopRecommender.recommendation  = "HPDG"
        
    @Rule(Usage('gaming and design') & Price('Medium'))
    def recommend_gaming_design_medium_price(self):
        LaptopRecommender.recommendation = "GPDG"

    @Rule(Usage('gaming and design') & Price('Low'))
    def recommend_gaming_design_low_price(self):
        LaptopRecommender.recommendation = "BGDG"

    @Rule(Usage('desk work') & Price('High'))
    def recommend_desk_work_high_price(self):
        LaptopRecommender.recommendation = "HQLD"

    @Rule(Usage('desk work') & Price('Medium'))
    def recommend_desk_work_medium_price(self):
        LaptopRecommender.recommendation = "RLDW"

    @Rule(Usage('desk work') & Price('Low'))
    def recommend_desk_work_low_price(self):
        LaptopRecommender.recommendation = "BFLW"

    @Rule(Usage('engineering') & Price('High'))
    def recommend_engineering_high_price(self):
        LaptopRecommender.recommendation = "PLET"

    @Rule(Usage('engineering') & Price('Medium'))
    def recommend_engineering_medium_price(self):
        LaptopRecommender.recommendation="LGPE"

    @Rule(Usage('engineering') & Price('Low'))
    def recommend_engineering_low_price(self):
        LaptopRecommender.recommendation="BFLE"
