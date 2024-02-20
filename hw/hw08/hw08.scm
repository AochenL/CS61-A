;(rle (list 1 1 1 2 2))
(define (rle s) 
    (cond
        ((null? s) nil)
        (else (cons-stream (helper (car s) s 0) (rle (next (car s) s))))
    )
)

;return the first repeated stream in s
;>(helper 1 (list 1 1 1 2 2) 0)
;>(1 3)
(define (helper curr s num)
    (cond
        ((and (not (null? s)) (eq? (car s) curr) ) (helper curr (cdr-stream s) (+ 1 num)))
        (else (list curr num))
    )
)
;return what is left in s after the first repeated stream
;>(next 1 (list 1 1 1 2 3 4))
;>(2 3 4)
(define (next curr s)
     (cond 
        ((null? s) nil)
        ((eq? (car s) curr) (next curr (cdr-stream s)))
        (else s)
    )
)

;>(group-by-nondecreasing (list 1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
;>(1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)

(define (group-by-nondecreasing s)
    (cond
        ((null? s) nil)
        (else (cons-stream (helper_group (car s) s ()) (group-by-nondecreasing (next_group (car s) s))))
    )
)

;return the first nondecreasing stream in s
;>(helper_group 1 (list 1 2 3 4 1 1 1 2) ())
;>(1 2 3 4)
(define (helper_group curr s ans)
    (cond
        ((and (not (null? s)) (>= (car s) curr)) (helper_group (car s) (cdr-stream s) (append ans (list (car s)))))
        (else ans)
    )
)

;return what is left in s after the nondecreasing stream
;>>(next_group 1 (list 1 2 3 4 1 1 1 2))
;>>(1 1 1 2)
(define (next_group curr s)
    (cond 
        ((null? s) nil)
        ((>= (car s) curr) (next_group (car s) (cdr-stream s)))
        (else s)
    )
)



(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

