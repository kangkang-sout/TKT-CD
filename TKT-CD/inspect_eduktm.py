import EduKTM, inspect, sys

print('MODULE_FILE:', getattr(EduKTM, '__file__', 'package'))
DKT = getattr(EduKTM, 'DKT', None)
print('DKT exists:', DKT is not None)
print('PYTHON:', sys.version)
if DKT is not None:
    try:
        print('SIGNATURE:', inspect.signature(DKT))
    except Exception as e:
        print('SIGNATURE_ERR:', e)
    try:
        print('\nSOURCE:\n')
        print(inspect.getsource(DKT))
    except Exception as e:
        print('GETSOURCE_ERR:', e)
else:
    print('EduKTM.DKT not found')
