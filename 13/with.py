try:
  with open('sample_file','w') as ff:
    for zaiko in zaikos:
      ff.write(str(zaiko)+'\n')
except:
  print ('エラーがおきました')