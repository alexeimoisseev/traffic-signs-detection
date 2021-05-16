from PIL import Image

data_dir = 'data/SwedishSigns'
output_dir = 'data/SwedishSigns'

annotations_file = open(data_dir + '/annotations.txt')
annotations_lines = annotations_file.readlines()

images = {}
labels_all = {
  ' 30_SIGN': 0,
  ' 50_SIGN': 1,
  ' 60_SIGN': 2,
  ' 70_SIGN': 3,
  ' 80_SIGN': 4,
  ' 90_SIGN': 5,
  ' 100_SIGN': 6,
  ' 110_SIGN': 7,
  ' 120_SIGN': 8,
  ' GIVE_WAY': 9,
  ' NO_PARKING': 10,
  ' NO_STOPPING_NO_STANDING': 11,
  ' PASS_EITHER_SIDE': 12,
  ' PASS_LEFT_SIDE': 13,
  ' PASS_RIGHT_SIDE': 14,
  ' PEDESTRIAN_CROSSING': 15,
  ' PRIORITY_ROAD': 16,
  ' STOP': 17,
  ' URDBL': 18,
  ' OTHER': 19,
}

labels = {
  'SPEED_LIMIT': 0,
  'OTHER': 1
}


def parse_boxes(input):
  items = input.replace('\n', '').split(';')
  result = []
  for item in items:
    if len(item) < 2:
      continue
    values = item.split(',')
    if len(values) < 2:
      continue
    [visibility, x2, y2, x1, y1, sign_type, label] = values

    abs_width = float(x2) - float(x1)
    abs_height = float(y2) - float(y1)
    abs_x = float(x1) + abs_width / 2
    abs_y = float(y1) + abs_height / 2
    img = Image.open(data_dir + '/images/' + filename)
    (im_width, im_height) = img.size
    x = abs_x / im_width
    y = abs_y / im_height

    width = abs_width / im_width
    height = abs_height / im_height
    simple_label = 'OTHER'
    if label.find('_SIGN') != -1:
      simple_label = 'SPEED_LIMIT'

    labelid = labels[simple_label]
    out = f'{labelid} {x:.5f} {y:.5f} {width:.5f} {height:.5f}'
    result.append(out)
  return result

def prepare_config():
  labelcount = len(labels.keys())
  labelarray = [None] * labelcount
  for key in labels:
    labelarray[labels[key]] = key
  return f'''train: \'{data_dir}/images/\'
val: \'{data_dir}/images/\'

nc: {labelcount}

names: {str(labelarray)}
  '''


for line in annotations_lines:
  (filename, boxes) = line.split(':')
  result = parse_boxes(boxes)
  images[filename] = result

print(len(images))
print(labels)
config = prepare_config()
with open(output_dir + '/swedish_signs.yml', 'w') as f:
  f.write(config)
  f.close()


for key in images.keys():
  filename = key.replace('jpg', 'txt')
  with open(output_dir + '/labels/' + filename, 'w') as f:
    for line in images[key]:
      f.write(line + '\n')
    f.close()