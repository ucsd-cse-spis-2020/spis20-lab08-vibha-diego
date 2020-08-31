from flask import Flask

app = Flask(__name__)



@app.route("/")

def hello():

   return "Hello World!"



def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)



@app.route('/ftoc/<ftemp_str>')

def convert_ftoc(ftemp_str):

    ftemp = 0.0

    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"






def miles_to_km(miles) :
  return (miles // 5) * 8

@app.route('/mtokm/<miles_str>')

def convert_mtokm(miles_str):

  miles = 0.0

  try:

    miles = float(miles_str)

    kilometers = miles_to_km(miles)

    return "In miles: " + miles_str + " In Kilometers" + str(kilometers)
    
  except ValueError:
  
    return "Sorry. Could not convert " + miles_str + " to a number"




def km_to_miles(km) :
  return (km // 8) * 5

@app.route( '/kmtom/<km_str')




def convert_kmtom(km_str):

  km = 0.0

  try:
    km = float(km_str)

    miles = km_to_m(km)

    return "In km: " + km_str + " In miles" + str(miles)

  except ValueError:

     return "Sorry. Could not convert " + km_str + " to a number"



if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os

from flask import Flask, url_for, render_template, request



app = Flask(__name__)



@app.route('/')

def render_main():

    return render_template('home.html')



@app.route('/ctof')

def render_ctof():

    return render_template('ctof.html')



@app.route('/ftoc')

def render_ftoc():

    return render_template('ftoc.html')



@app.route('/mtokm')

def render_mtokm():

    return render_template('mtokm.html')

@app.route('/kmtom')
def render_kmtom():
  return render_template('kmtom.html')
    

@app.route('/ftoc-result')

def render_ftoc_result():

    try:

        ftemp_result = float(request.args['ftemp'])

        ctemp_result = ftoc(ftemp_result)

        return render_template('ftoc_result.html', ftemp=ftemp_result, ctemp=ctemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/ctof-result')

def render_ctof_result():

    try:

        ctemp_result = float(request.args['ctemp'])

        ftemp_result = ctof(ctemp_result)

        return render_template('ctof_result.html', ctemp=ctemp_result, ftemp=ftemp_result)

    except ValueError:

        return "Sorry: something went wrong."



@app.route('/mtokm-result')

def render_mtokm_result():

    try:

        # You'll need some code here, and maybe some extra parameters in render_template below...

        return render_template('mtokm.html')

    except ValueError:

        return "Sorry: something went wrong."


@app.route('/kmtom-result')

def render_kmtom_result():

    try:

        # You'll need some code here, and maybe some extra parameters in render_template below...

        return render_template('kmtom.html')

    except ValueError:

        return "Sorry: something went wrong."



def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)

    

def ctof(ftemp):

   return -42.0 # replace with correct formula



# You'll probably want a basic function here to convert miles to kilometers too...

    

if __name__=="__main__":

    app.run(host='0.0.0.0')
    