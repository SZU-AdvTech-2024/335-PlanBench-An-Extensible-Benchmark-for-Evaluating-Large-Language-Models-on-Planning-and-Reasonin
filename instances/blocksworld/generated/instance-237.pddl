(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects d l e a g k j h f c i b)
(:init 
(handempty)
(ontable d)
(ontable l)
(ontable e)
(ontable a)
(ontable g)
(ontable k)
(ontable j)
(ontable h)
(ontable f)
(ontable c)
(ontable i)
(ontable b)
(clear d)
(clear l)
(clear e)
(clear a)
(clear g)
(clear k)
(clear j)
(clear h)
(clear f)
(clear c)
(clear i)
(clear b)
)
(:goal
(and
(on d l)
(on l e)
(on e a)
(on a g)
(on g k)
(on k j)
(on j h)
(on h f)
(on f c)
(on c i)
(on i b)
)))