from pathlib import Path 
import argparse
import os

def concat_files(file1_path,file2_path,output_path):
    with open(file1_path) as f :
        origin_data = [line for line in f]

    with open(file2_path) as f :
        merimen_data = [line for line in f]

    addition = [line for line in merimen_data if line not in origin_data]
    
    print('duration :',len(merimen_data)-len(addition))
    print('addition :',len(addition))
    
    origin_data.extend(addition)

    with open(output_path,'w') as f:
        for line in origin_data:
            f.write(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file',type=str,help='path to first file')
    parser.add_argument('second_file',type=str,help='path to second file')
    parser.add_argument('output_file',type=str,help='path to output file')

    args = parser.parse_args()

    concat_files(args.first_file, args.second_file, args.output_file)

    #move data
    output_label_path = args.output_file.replace('.txt','')
    first_label_path = args.first_file.replace('.txt','')
    second_label_path = args.second_file.replace('.txt','')

    Path(output_label_path).mkdir(parents=True,exist_ok=True)

    os.system('cp '+first_label_path+'/* '+output_label_path)
    os.system('cp '+second_label_path+'/* '+output_label_path)

if __name__ == '__main__':
    main()