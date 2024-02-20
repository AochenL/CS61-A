
(define (split-at lst n)
	;>(split-at (1 2 3 4 5) 3)
	;>((1 2 3) 4 5)
	;scm> (define new (list (list 1 2 3) 4 5))
	;new
	;scm> (cdr new)
	;(4 5)
	;scm> (car new)
	;(1 2 3)
  (define (first lst n)
	;returns a list that contains first n elements of lst
	;> (define lst (1 2 3 4 5))
	;>(first lst 3)
	;>(1 2 3)
	;>(first lst 7)
	;>(1 2 3 4 5)
	(cond ((= n 0) nil)
		  ((null? lst) nil)
		  (else (cons (car lst) (first (cdr lst) (- n 1))))
	)
  )
  
  (define (last lst n)
	;returns what is left of a list after the first n elements has been removed
	;>(last (list 1 2 3 4 5) 3)
	;>(4 5)
	;>(last (list 1 2 3 4 5) 7)
	;>()
	(cond ((= n 0) lst)
		  ((null? lst) nil)
		  (else (last (cdr lst) (- n 1)))
	)
  )
  (cons (first lst n) (last lst n))
)


(define-macro (switch expr cases)
	(cons _________
		(map (_________ (_________) (cons _________ (cdr case)))
    			cases))
)

;(eq? expr (car (car cases))) 
;(define cases  (list ,(1 (print 'a)) (2 (print 'b)) (3 (print 'c))))

