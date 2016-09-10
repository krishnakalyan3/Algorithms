import scala.io.StdIn

object AplusB {
  def main(args: Array[String]): Unit = {
    val rawInput = StdIn.readLine()
    val nums = rawInput.split(" ")
    val add = nums(0).toInt + nums(1).toInt
    println(add)
  }
}
