import os

def is_forked():
  try:
    os.environ['fork tracking']
    return False
  except:
    return True

def overwrite(msg):
  with open('main.py','w') as f:
    f.write(msg)

  
  