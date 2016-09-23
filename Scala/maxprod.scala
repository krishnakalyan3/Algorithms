import scala.io.StdIn

/**
  * Created by krishna on 11/09/16.
  */
object maxprod {
  def main(args: Array[String]): Unit = {
    val n = StdIn.readLine().toInt
    val nums = StdIn.readLine().split(" ").map(x => x.toInt)

    assert(n == nums.length)

    var maxno1:Long = 0
    var maxno2:Long = 0
    var index1 = 0
    for( index <- nums.indices){
      if (nums(index) > maxno1) {
          maxno1 = nums(index)
          index1 = index
      }
    }
    for( index <- nums.indices){
      if (index1 != index) {
        if(nums(index) > maxno2){
          maxno2 = nums(index)
        }
      }
    }
    println(maxno1 * maxno2)

  }

}
