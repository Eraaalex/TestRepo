
import sys
sys.path.append('../ORM')

from models import *
from service import *

a=addFeedback(login='None4@none.com',text='Not Bad')
# db.session.commit()
fb=getFeedback()
print(fb,len(fb), sep='\n')
