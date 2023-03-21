from flask import Flask,render_template, redirect, url_for, request
import sklearn
import pickle

model=pickle.load(open("Model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/show/<pred>")
# def show(pred):
#      return render_template("show.html",pred=pred)


@app.route("/predict",methods=["POST","GET"])
def prediction():
    if request.method=="POST":
        #kms driven
        kms_driven=request.form["Kms_Driven"]

        ##cars
        cars=request.form["Cars_Names"]
        brio=0
        riaz=0
        city=0
        corolla_altis=0
        fortuner=0
        grand_i10=0
        i20=0
        innova=0
        verna=0

        if cars=="Brio":
            brio=1
            riaz=0
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=0
            innova=0
            verna=0

        elif cars=="Riaz":
            brio=0
            riaz=1
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=0
            innova=0
            verna=0  

        elif cars=="City":
            brio=0
            riaz=0
            city=1
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=0
            innova=0
            verna=0    

        elif cars=="Corolla_Altis":
            brio=0
            riaz=0
            city=0
            corolla_altis=1
            fortuner=0
            grand_i10=0
            i20=0
            innova=0
            verna=0

        elif cars=="Fortuner":
            brio=0
            riaz=0
            city=0
            corolla_altis=0
            fortuner=1
            grand_i10=0
            i20=0
            innova=0
            verna=0

        elif cars=="Grand_i10":
            brio=0
            riaz=0
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=1
            i20=0
            innova=0
            verna=0

        elif cars=="i20":
            brio=0
            riaz=0
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=1
            innova=0
            verna=0

        elif cars=="Innova":
            brio=0
            riaz=0
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=0
            innova=1
            verna=0

        elif cars=="Verna":
            brio=0
            riaz=0
            city=0
            corolla_altis=0
            fortuner=0
            grand_i10=0
            i20=0
            innova=0
            verna=1

        ##number of years
        number_of_years=request.form["Number_Of_Year"]

        ##Fuel Type
        fuel_type=request.form["Fuel_Type"]
        petrol=0
        diesel=0
        if fuel_type=="Diesel":
            petrol=0
            diesel=1
        elif fuel_type=="Petrol":
            petrol=1
            diesel=0

        ##seller type
        seller_type=request.form["Seller_Type"]
        dealer=0
        individual=0

        if seller_type=="Dealer":
                    dealer=1
                    individual=0

        if seller_type=="Individual":
                    dealer=0
                    individual=1
        
        ##Transmission
        transmission=request.form["Transmission"]
        automatic=0
        manual=0

        if transmission=="Automatic":
                  automatic=1
                  manual=0   

        if transmission=="Manual":
                  automatic=0
                  manual=1

        d={"kms_driven":kms_driven,"Cars":{"brio":brio,
                                           "riaz":riaz,
                                           "city":city,
                                           "corolla_altis":corolla_altis,
                                           "fortuner":fortuner,
                                           "grand_i10":grand_i10,
                                           "i20":i20,
                                           "innova":innova,
                                           "verna":verna},
                                           "Number of Years":number_of_years,
                                           "Fuel Type":{"Petrol":petrol,"Diesel":diesel},
                                           "Seller_type":{"Dealer":dealer,"Individual":individual},
                                           "Transmission":{"Automatic":automatic,"Manual":manual}
                                             }
        
        pred=model.predict([[kms_driven,
                               brio,
                               riaz,
                               city,
                               corolla_altis,
                               fortuner,
                               grand_i10,
                               i20,
                               innova,
                               verna,
                               number_of_years,
                               petrol,
                               diesel,
                               dealer,
                               individual,
                               automatic,
                               manual
                               ]])
        pred=round(pred[0],2)
        return render_template("show.html",p=pred)




if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
