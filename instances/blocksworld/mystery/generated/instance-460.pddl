(define (problem BW-generalization-4)
(:domain mystery-4ops)(:objects c d b h l g f k)
(:init 
(harmony)
(planet c)
(planet d)
(planet b)
(planet h)
(planet l)
(planet g)
(planet f)
(planet k)
(province c)
(province d)
(province b)
(province h)
(province l)
(province g)
(province f)
(province k)
)
(:goal
(and
(craves c d)
(craves d b)
(craves b h)
(craves h l)
(craves l g)
(craves g f)
(craves f k)
)))