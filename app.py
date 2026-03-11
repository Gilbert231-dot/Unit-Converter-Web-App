from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = None
    from_unit = None
    to_unit = None
    value = None

    if request.method == 'POST':
        value = request.form.get('value')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')      
    
        if value and from_unit and to_unit:
            try:
                value = float(value)
                if from_unit == 'kilometers' and  to_unit == 'miles':
                    result = value * 0.621371      
                elif from_unit == 'miles' and to_unit == 'kilometers':
                    result = value * 1.60934            
                elif from_unit == 'meters' and  to_unit == 'feet':
                    result =value * 3.28084         
                elif from_unit == 'feets' and to_unit == 'meters':
                    result =value * 0.3048       
                elif from_unit == 'centimeters' and  to_unit == 'inches':
                    result = value * 0.393701       
                elif from_unit == 'inches'and to_unit == 'centimeters':
                    result =value * 2.54           
                elif from_unit == 'kilometers' and  to_unit == 'meters':
                    result =value * 1000            
                elif from_unit == 'meters' and to_unit == 'centimeters':
                    result =value * 100             
                elif from_unit == 'miles'  and  to_unit == 'yards':
                    result =value * 1760     
                elif from_unit == 'yards'  and  to_unit == 'meters':
                    result =value * 0.9144
            except ValueError: 
                result= "Wrong value! Input a number" 
    return render_template('length.html',
                           from_unit=from_unit,
                            to_unit=to_unit,
                            value=value,
                            result=result
                        )

    
@app.route('/time', methods=['GET','POST'])
def time_converter():
    result = None
    from_unit = None
    to_unit = None
    value = None

    if request.method == 'POST':
        value = request.form.get('value')
        from_unit = request.form.get('from_unit')
        to_unit = request.form.get('to_unit')

        if value and from_unit and to_unit:
            try:
                value = float(value)
                if from_unit == 'hours' and to_unit == 'minutes':
                    result = value * 60  
                elif from_unit == 'minutes' and to_unit == 'seconds':
                    result = value * 60
                elif from_unit == 'hours' and to_unit == 'seconds':
                    result = value * 3600
                elif from_unit == 'days' and to_unit == 'hours':
                    result = value * 24
                elif from_unit == 'weeks' and to_unit == 'days':
                    result = value * 7
                elif from_unit == 'years' and to_unit == 'days':
                    result = value * 365
                elif from_unit == 'months' and to_unit == 'days':
                    result = value * 30.44
            except ValueError:
                result = 'Wrong value! Input a number'
    return render_template('time.html',
                        from_unit=from_unit,
                        to_unit=to_unit,
                        value=value,
                        result=result
                        )
    
if __name__== "__main__":
    app.run(debug=True)