(define (reverse lst)
    (define (len lst)
    ; return the length of lst
        (cond ((null? lst) 0)
              (else (+ 1 (len (cdr lst))))
        )
    )
    (define (helper lst n)
    ; reverse lst whose length is n
        (cond ((= 0 n) lst)
              (else (append (helper (cdr lst) (- n 1)) (list (car lst))))
        )
    )
    (helper lst (len lst))

)

;An alternative solution
;(define (reverse lst)
 ;   'YOUR-CODE-HERE
  ;  (if (null? lst) nil
    ;    (append (reverse (cdr lst)) (list (car lst)))
   ; )
;)

