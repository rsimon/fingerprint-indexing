import json
import random

# Creates a random bar chart value.
# 50% chance of having a value != 0. If it has a value,
# it's a value between 0 and 1.
def newRandomValue():
  rand = random.uniform(0, 1)
  if rand > 0.5:
    return random.uniform(0, 1)
  else:
   return 0

# Creates a random 'block' of bars.
# 30% chance of having any bars. If it has bars, it uses
# newRandomValue() to generate the bars.
def newRandomBlock(prefix):
  rand = random.uniform(0, 1)
  block = {}
  if rand > 0.7:
    block[prefix + '_mono_fine'] = newRandomValue()
    block[prefix + '_mono_coarse'] = newRandomValue()
    block[prefix + '_matt_painted'] = newRandomValue()
    block[prefix + '_impressed'] = newRandomValue()
    block[prefix + '_black_glazed'] = newRandomValue()
  else:
    block[prefix + '_mono_fine'] = 0
    block[prefix + '_mono_coarse'] = 0
    block[prefix + '_matt_painted'] = 0
    block[prefix + '_impressed'] = 0
    block[prefix + '_black_glazed'] = 0

  return block

def newRandomSpecialCategoryBlock():
  rand = random.uniform(0, 1)
  if rand > 0.8:
    return {
      'archaika': newRandomValue(),
      'defunct': newRandomValue(),
      'miniatures': newRandomValue()
    }
  else:
    return {
      'archaika': 0,
      'defunct': 0,
      'miniatures': 0
    }

# Creates a random fingerprint row, using newRandomBlock
def newRandomRow():
  row = newRandomBlock('local')
  row.update(newRandomBlock('regional'))
  row.update(newRandomBlock('loc_reg'))
  row.update(newRandomBlock('import'))
  row.update(newRandomSpecialCategoryBlock())
  return row

# Creates a new random assemblage fingerprint
def newRandomAssemblage():
  return {
    'sector': '',
    'layer_context': '',
    'date': {
      'from': 0,
      'to': 0
    },
    'fp_ceramic': {
      'longterm_storage': newRandomRow(),
      'shortterm_storage': newRandomRow(),
      'preparation_cooking': newRandomRow(),
      'food': newRandomRow(),
      'mixing_drinks': newRandomRow(),
      'serving_drinks': newRandomRow(),
      'consuming_drinks': newRandomRow(),
      'perfumes_fragrances': newRandomRow(),
      'light': newRandomRow(),
      'storage_non_edible': newRandomRow(),
      'unidentified': newRandomRow()
    }
  }

assemblages = [
  newRandomAssemblage(),
  newRandomAssemblage(),
  newRandomAssemblage(),
  newRandomAssemblage()
]

print(json.dumps(assemblages, indent=2))
