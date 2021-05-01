
import re

def transform_csv(file_path: str) -> list:
    output_lines = []
    with open(file_path, "r") as f:
        for line in f:
            line_split = line.split(',')
            # filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes
            # set_2_0001.jpg,118811, 1 
            # "{}", 2 
            # 10, 3
            # 0, 4 
            # "{""name"":""rect"", 5  
            # ""x"":1062,6
            # ""y"":607,7
            # ""width"":194, 8
            # ""height"":240}", 9
            # "{}" 10
            # 0
            if(len(line_split) != 11):
                print(line)
                continue
            # 0        1  2  3  4  5      6      7          8       
            (fileName, _, _, _, _, _,x_str, y_str, width_str, height_str,_) = line_split
            width = re.findall("\d+",width_str)[0]
            height = re.findall("\d+", height_str)[0]
            x1 = int(re.findall("\d+",x_str)[0])
            x2 = x1 + int(width)
            y1 = int(re.findall("\d+",y_str)[0])
            y2 = y1 + int(height)
            transformed_line = ",".join([fileName, str(x1), str(x2), str(y1), str(y2), "Chicken"])
            output_lines.append(transformed_line + "\n")
    return output_lines
    
if __name__ == "__main__" :
    output_lines = transform_csv("Chicken_Images_Set3_Set2_csv.csv")
    with open("parsed.csv", "w") as f_w:
        f_w.writelines(output_lines)