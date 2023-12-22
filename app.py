from flask import Flask, render_template, request

from recommendation_system.LaptopRecommender import LaptopRecommender
from recommendation_system.Usage import Usage
from recommendation_system.Price import Price

from models.Dataset import Dataset

laptop_recommender = LaptopRecommender()
data = Dataset("models/processed_dataset_urls.csv")

app = Flask(__name__)

recommender = {
    # gaming and design
    "HPDG": {
        "message": "High-performance gaming laptops for design and gaming are recommended",
        "subset" : data.get_gaming_design_high()
    },
    "GPDG": {
        "message": "Gaming laptops with good performance for design and gaming are recommended.",
        "subset": data.get_gaming_design_medium()
    },
    "BGDG": {
        "message": "Budget-friendly gaming laptops for design and gaming are recommended.",
        "subset": data.get_gaming_design_low()
    },

    # desk work
    "HQLD": {
        "message": "High-quality laptops for desk work are recommended.",
        "subset": data.get_desk_work_data_high()
    },
    "RLDW": {
        "message": "Reliable laptops for desk work are recommended.",
        "subset": data.get_desk_work_data_medium()
    },
    "BFLW": {
        "message": "Budget-friendly laptops for desk work are recommended.",
        "subset": data.get_desk_work_data_low()
    },

    # engineering
    "PLET": {
        "message": "Powerful laptops for engineering tasks are recommended.",
        "subset": data.get_engineering_data_high()
    },
    "LGPE": {
        "message": "Laptops with good performance for engineering tasks are recommended.",
        "subset": data.get_engineering_data_medium(),
    },
    "BFLE": {
        "message": "Budget-friendly laptops for engineering tasks are recommended.",
        "subset": data.get_engineering_data_low()
    }
}



@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

		# parse input from request
        price_input = request.form['price']
        usage_input = request.form['usage']
		
        # initialize recommender
        laptop_recommender.reset()
        laptop_recommender.declare(Usage(usage_input))
        laptop_recommender.declare(Price(price_input))
        laptop_recommender.run()
        
        recommendation = laptop_recommender.recommendation

        message = recommender[recommendation]["message"]
        subset = recommender[recommendation]["subset"]

        return render_template("show_recommendation.jinja", message=message, subset=subset)

    return render_template("index.jinja")




if __name__ == '__main__':
    app.run(debug=True)