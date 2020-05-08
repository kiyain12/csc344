
abstract class S {
  def eval(env: (String, Int)): (Boolean, Int)
}

case class E(left: T, right: Option[E2]) extends S {

  def eval(env:(String, Int)):(Boolean, Int)={

    val EvaluatedLeft = left.eval((env._1, env._2))
    if (EvaluatedLeft._1) {
      (true, EvaluatedLeft._2)

    } else right match {

      case None => (false, -1)

      case Some(r) => {
        val EvaluateOther = r.eval((env._1, env._2))
        if(EvaluateOther._1) {
          (true, EvaluateOther._2)
        } else (false, -1)
      }
    }
  }
}
case class E2(left: E3) extends S {
  def eval(env: (String, Int)):(Boolean, Int) = left.eval(env._1, env._2)

}

case class E3(left: T, right: Option[E2]) extends S{
def eval(env:(String, Int)):(Boolean, Int)={

  val EvaluatedLeft = left.eval((env._1, env._2))
  if (EvaluatedLeft._1) {
    (true, EvaluatedLeft._2)
  } else right match {

    case None => (false, -1)

    case Some(r) => {
      val EvaluateOther = r.eval((env._1, env._2))
      if(EvaluateOther._1) {
        //(false, EvaluateOther._2)
        (true, EvaluateOther._2)
      } else (false, -1)
    }
  }
}
}
case class T(left: F, right: Option[T2]) extends S {
  def eval(env:(String, Int)):(Boolean, Int)={

    val EvaluatedLeft = left.eval((env._1, env._2))
    right match {
      case None => EvaluatedLeft

      case Some(r) => if(!EvaluatedLeft._1) {
        (false, -1 )
      } else {
      val EvaluatedOther = r.eval((env._1, EvaluatedLeft._2))
      if (EvaluatedOther._1) {
        (true, EvaluatedOther._2)
      } else (false, -1)
      }
    }
    }
}

//FAIL CASE
case class T2(left: F, right: Option[T2]) extends S {
  def eval(env:(String, Int)):(Boolean, Int)={

    val EvaluatedLeft = left.eval((env._1, env._2))
    if (!EvaluatedLeft._1) (false, -1)
    else right match {
      case None => EvaluatedLeft
      case Some(r) => {
        val EvaluatedOther = r.eval((env._1, EvaluatedLeft._2))
        if (EvaluatedOther._1) {
          (true, EvaluatedOther._2)
        } else (false, -1)
      }
    }
  }

}
case class F(left: A, right: Option[F2]) extends S {
  def eval(env: (String, Int)): (Boolean, Int) = {
    val EvaluatedLeft = left.eval(env._1, env._2)
  right match {
    case None => EvaluatedLeft
    case Some(_) => if (!EvaluatedLeft._1) {
      (true, env._2)
    } else EvaluatedLeft
  }
  }
}
case class F2(left: Option [F2]) extends S {
  def eval(env: (String, Int)): (Boolean, Int) = null
}

abstract class A extends S

case class A2(left: E) extends A {
  def eval(env: (String, Int)): (Boolean, Int) = left.eval(env._1,env._2)
}
case class C(term: Char) extends A {
  override def eval(env: (String, Int)): (Boolean, Int) = {
    if (env._1.charAt(env._2) == term || term == '.') {
      (true, env._2 + 1)
    }
    else (false, -1)
  }
}

class Recursive_Parsing(input: String){
  var index = 0

  def parseS(): E = parseE()
  def parseE() = E(parseT(), parseE2())
  def parseE2(): Option[E2] = {
    if (index < input.length && input(index) == '|'){
      index+=1;
      Some(E2(parseE3()))
    }
    else None
  }
  def parseE3(): E3 = E3(parseT(), parseE2())
  def parseT(): T = T(parseF(), parseT2())
  def parseT2(): Option[T2] = {
    if (index < input.length && (input(index) == '.'|| input(index) == '(' || input(index) == ' '|| input(index).isLetterOrDigit)){
    //  index+=1;
      Some(T2(parseF(), parseT2()))
    }
    else None
  }
  def parseF(): F = F(parseA(), parseF2())

  def parseF2(): Option[F2] = {
    if (index < input.length && input(index) == '?'){
      index+=1;
      Some(F2(parseF2()))
    }
    else None
  }
  def parseA(): A = {
    if (index < input.length && input(index) == '(' ){
      index += 1
      parseA2()
    } else {
      val c = C(input(index))
      index += 1
      c
    }
  }

  def parseA2(): A2 = {
    val a = A2(parseE())
    if (index < input.length && input(index)== ')'){
      index+=1;
      a
    }
    else throw new RuntimeException()
  }
}

//case class C(left: Option[String], right: Option[Int]) extends Sv2
object Main{

  def main(args: Array[String]){

   print("pattern?")

    val pattern = scala.io.StdIn.readLine()

    val x = new Recursive_Parsing(pattern)

    print("string?")

    var kb = scala.io.StdIn.readLine()
    val exp2rd:S = x.parseE()
    while (kb != "let me out"){
      def result (env: String): String = {
        val EvaluatedExp2rd = exp2rd.eval(kb, 0)
        if (EvaluatedExp2rd._1 && EvaluatedExp2rd._2 == kb.length){


          "match"
        } else "no match"
      }
      println(result(kb))
      print("string?")
      kb = scala.io.StdIn.readLine()
    }


  }



}