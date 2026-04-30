import traceback
try:
 raise Exception('This is the error message.')
except:
   errorFile = open('errorInfo.txt', 'w')

   errorFile.write(traceback.format_exc())

   errorFile.close()
   print('The traceback info was written to errorInfo.txt.')
'''
حلوي اوي ديه علشان تقدر تعرف فين الخطأ حصل بالظبط في الكود بتاعك
و تقدر تتابع الخطوات اللي حصلت قبل ما يحصل الخطأ و كمان تعرف نوع الخطأ اللي حصل
و تقدر تكتب كل ده في ملف علشان تراجعه بعدين و تصلح الخطأ بسهولة
'''