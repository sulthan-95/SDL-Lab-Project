from flask_wtf import Form
from wtforms import StringField,BooleanField,IntegerField,DecimalField
from wtforms.validators import DataRequired

class SymptomsForm(Form):
	age=IntegerField('age',validators=[DataRequired()])
	bp=IntegerField('bp',validators=[DataRequired()])
	specific_gravity=DecimalField('sg',validators=[DataRequired()],places=1,rounding=None)
	sugar=IntegerField('sugar',validators=[DataRequired()])
	blood_glucose_random=IntegerField('bgc',validators=[DataRequired()])
	blood_urea=IntegerField('bu',validators=[DataRequired()])
	serum=IntegerField('sc',validators=[DataRequired()])
	sodium=IntegerField('sodium',validators=[DataRequired()])
	potassium=IntegerField('potassium',validators=[DataRequired()])
	hemoglobin=IntegerField('hg',validators=[DataRequired()])
	packed_cell_volume=IntegerField('pcv',validators=[DataRequired()])
	wbc=IntegerField('wbc',validators=[DataRequired()])
	rbc=IntegerField('rbc',validators=[DataRequired()])
	pus_cell=IntegerField('pus',validators=[DataRequired()])
	pus_cell_clumps=BooleanField('pcc',validators=[DataRequired()],default=false)
	bacteria=BooleanField('bac',validators=[DataRequired()],default=false)
	hypertension=BooleanField('ht',validators=[DataRequired()],default=false)
	diabetes=BooleanField('dbm',validators=[DataRequired()],default=false)
	cad=BooleanField('cad',validators=[DataRequired()],default=false)
	appetite=BooleanField('app',validators=[DataRequired()],default=false)
	pedal=BooleanField('ped',validators=[DataRequired()],default=false)
	anemia=BooleanField('anemia',validators=[DataRequired()],default=false)
