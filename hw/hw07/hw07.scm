(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))

(define (caddr s)
  (car(cdr (cdr s))))


(define (sign num)
  (cond ((< num 0) -1) ((= num 0) 0) (else 1))
)


(define (square x) (* x x))

(define (pow x y)
  (cond ((= y 1) x) 
        ((even? y) (square (pow x (/ y 2)))) 
        (else (* x (square (pow x (/ (- y 1) 2))))))
)

(define (remove num s)
  (filter (lambda (x) (not (eq? num x))) s)
)

(define (unique s)
  (cond ((null? s) nil)
        (else (cons (car s) (unique(remove (car s) (cdr s))))))
)


(define (replicate x n)
  (define (replicate_helper x n s)
    (cond ((eq? n 0) s)
          (else (replicate_helper x (- n 1) (cons x s)))))
  (replicate_helper x n ())
)


(define (accumulate combiner start n term)
  (cond ((eq? n 0) start)
        (else (accumulate combiner (combiner start (term n)) (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (cond ((eq? n 0) start)
        (else (accumulate combiner (combiner start (term n)) (- n 1) term))
  )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

(map (lambda (x) (* x x))  (filter (lambda (x) (odd? x)) '(3 4 5)))

(define (map-reverse s m)
 (if (null? s)
 m
 (map-reverse (cdr s)
 (cons (procedure (car s))
 m)) ))

 (define (map procedure s)
 (if (null? s) nil
      (cons (procedure (car s))
      (map procedure (cdr s))) ) )

(define (tail_map procedure s)
  (define (helper procedure s m)
    (cond 
      ((null? s) m)
      (else (helper procedure (cdr s) (cons(procedure (car s)) m))))
    )
  (helper procedure s ())
)



(define (procedure x) (- 1 x)
     )

(map (lambda (x) (* x x)) '(2 3 4 5))

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals)
)

(define-macro (for sym vals expr)
  `(map (lambda (,sym) ,expr) ,vals)
)

(for x '(2 3 4 5) (* x x))

