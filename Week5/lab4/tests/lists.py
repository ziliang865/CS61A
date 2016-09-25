test = {
  'name': 'List Comprehension',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [x*x for x in range(5)]
          0a91f170cfa80795d72b5c0b9fdec8d8
          # locked
          >>> [n for n in range(10) if n % 2 == 0]
          b3c8f6284a07a24eacc329bd9818e1f7
          # locked
          >>> ones = [1 for i in ["hi", "bye", "you"]]
          >>> ones + [str(i) for i in [6, 3, 8, 4]]
          fbf9af6642897d5e364911eff687dd7d
          # locked
          >>> [i+5 for i in [n for n in range(1,4)]]
          64ae6caf27071172b64d4acbb955b9d8
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
