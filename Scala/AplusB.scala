object AplusB {
  def main(args: Array[String]): Unit = {
    val rawInput = readLine()
    val nums = rawInput.split(" ")
    println(nums(0).toInt + nums(1).toInt)
  }
}
