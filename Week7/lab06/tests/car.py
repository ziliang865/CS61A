test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          74c2147b5ba7769cc5f991cbfd7b8d69
          # locked
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          1a050ef9b8e68b745fd1986a9eba405f
          # locked
          >>> hilfingers_car.drive()
          568957c82681d74b2e26961d417b2328
          # locked
          >>> hilfingers_car.fill_gas()
          c0e5eff108e787b15de63424867085d6
          # locked
          >>> hilfingers_car.gas
          1987bce9c137ee1be913e29126e18d3c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> hilfingers_car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.num_wheels
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> hilfingers_car.drive()
          568957c82681d74b2e26961d417b2328
          # locked
          >>> Car.drive()
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> Car.drive(hilfingers_car)
          568957c82681d74b2e26961d417b2328
          # locked
          >>> MonsterTruck.drive(hilfingers_car)
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> sumukhs_car = MonsterTruck('Monster', 'Batmobile')
          >>> sumukhs_car.drive()
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.drive(sumukhs_car)
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> MonsterTruck.drive(sumukhs_car)
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.rev(sumukhs_car)
          34db8258c24aff02f4e0aeaa32af407b
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
