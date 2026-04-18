import pprint
import myCats
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
#"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\nprint(cats)\n')
#fileObj.write('catss = ' + str(cats) + '\nprint(cats)')
fileObj.close()
print(myCats.cats)
print(myCats.cats[1]['name'])
