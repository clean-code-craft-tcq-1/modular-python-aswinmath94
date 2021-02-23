from telecom_reference_manual import createReferenceManual
from telecom_reference_manual import printReferenceManual
import colorpair_num_test as tester

if __name__ == '__main__':
    tester.telecom_colorpair_num_test()
    print('*** Reference Manual ***')
    printReferenceManual(createReferenceManual())
    print('*** Done ***')
