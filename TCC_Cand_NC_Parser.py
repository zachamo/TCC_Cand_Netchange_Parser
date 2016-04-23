import glob

OUTPUT_NAME = 'output.csv'
FILE_LIST = glob.glob("*.csv")
MESSAGES = ['total.candidate=','total.candidate.delete=','total.candidate.create=',
            'total.candidate.update=','total.warning=','total.status.success=',
            'total.status.error=']

def csv_extract(filename):
    """ (file open for reading) -> output file
    Check for specified data in csv, extract into output
    """
    result_nums = []
    for i in range(len(MESSAGES)):
        result_nums.append('0')
    errors = []
    line_count = 0
    contents = open(filename)
    for line in contents:
        line_count += 1
        for msg in range(len(MESSAGES)):
            if MESSAGES[msg] in line:
                result_nums[msg] = (line[line.find("=")+1:len(line)].strip())
        if line[0]=='"' and "error" in line:
            errors.append(line.strip())
    return result_nums,errors,line_count

def list_to_nums(list_to_convert):
    """ (list of num as str) -> str
    remove quotations from provided str
    """
    output = ''
    for c in str(list_to_convert)[1:-1]:
        if c != "'":
            output += c
    return output
    
def read_and_write():
    """(Nonetype)
    Read each file, find MESSAGES, write output.
    """
    output = open(OUTPUT_NAME,'a')
    
    for file in FILE_LIST:
        result_nums,errors,line_count = csv_extract(file)
        output.write(file+'\n')
        
        if "candidate_scrubber" in file:
             output.write("Record count: "+str(line_count-1)+'\n')
             
        else:
            output.write(str(MESSAGES)[1:-1]+'\n')
            output.write(list_to_nums(result_nums)+'\n')
        
        output.write('Errors Below:\n')
        for error in errors:
            output.write(error+'\n')
            
        output.write('\n')
        
    output.close()


#Begin Program
print ("Files_to_analyze:",FILE_LIST)
proceed = input('Proceed: Y/N: ')
if proceed in ("y","Y"):
    read_and_write()
print('Complete')
