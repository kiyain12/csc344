(ns demo.core)

(def p1 '(and x(or x(and y (not z)))))
(def p2 '(and (and z false) (or x true false)))
(def p3 '(or true a))
(def p4 '(or x y false (and true (not (not (not z))))))
(def bindtest '{x false, z true})
(def e '(not x))
(def e1 '(and x y true))

(def t1 '(not x))
(def t2 '(and x y))
(def t3 '(and x y z))
(def t4 '(and w x y z))
(def t5 '(or x y))
(def t6 '(or x y z))
(def t7 '(or w x y z))


(defn fromNOTexptoNORv2 [e]
  (cons 'nor (rest e))
  )

(defn fromORexptoNOR [e]
  (cons 'nor (list (cons 'nor (rest e ))))

  )

(defn fromANDexptoNORv2 [e]
  (cons 'nor (map #(list 'nor %) (rest e)))

  )

(defn generalconvertv2 [e]
  (if (seq? e)
    (let [x (map #(generalconvertv2 %) e)]

                 (cond
                   (= (first x) 'not) (fromNOTexptoNORv2 x)
                   (= (first x) 'or) (fromORexptoNOR x)
                   (= (first x) 'and) (fromANDexptoNORv2 x)
                   ))e)
  )

(defn lookup [i m]
  (get m i i)
  )

(defn bindvaluesv2 [l m]
  (map (fn[i]
         (if (seq? i)
           (bindvaluesv2 i m)
           (get m i i)))

       l)
  )

(defn simplifymaster [l]
    (let [l (map (fn [n]
                   (if (seq? n) (simplifymaster n) n)) l)]
      (cond

        (every? false? (rest (distinct l))) true


        (some false? l) (simplifymaster (remove false? (distinct l)))


        (some true? l) false



        (and (= (count l) 2) (seq? (second l)))
          (if (= (count (second l)) 2)
            (second (second l))
            (distinct l))
          :else (distinct l))
      )
    )

(defn evalexp [exp bindings]
  (simplifymaster (generalconvertv2 (bindvaluesv2 exp bindings)))
  )



