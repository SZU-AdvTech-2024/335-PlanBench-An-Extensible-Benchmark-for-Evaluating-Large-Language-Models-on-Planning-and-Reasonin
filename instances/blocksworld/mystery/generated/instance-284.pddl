(define (problem BW-generalization-4)
(:domain mystery-4ops)(:objects h g j c i d l a e)
(:init 
(harmony)
(planet h)
(planet g)
(planet j)
(planet c)
(planet i)
(planet d)
(planet l)
(planet a)
(planet e)
(province h)
(province g)
(province j)
(province c)
(province i)
(province d)
(province l)
(province a)
(province e)
)
(:goal
(and
(craves h g)
(craves g j)
(craves j c)
(craves c i)
(craves i d)
(craves d l)
(craves l a)
(craves a e)
)))