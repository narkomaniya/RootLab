import java.io.BufferedReader
import java.io.InputStreamReader

private fun checkRoot(onResult: (String) -> Unit) {
    Thread {
        val result = try {
            val process = ProcessBuilder("su", "-c", "id")
                .redirectErrorStream(true)
                .start()

            val output = BufferedReader(
                InputStreamReader(process.inputStream)
            ).use { it.readText() }

            val exitCode = process.waitFor()
            if (exitCode == 0) output else "Ошибка: $output"
        } catch (e: Exception) {
            "Не удалось выполнить запрос: ${e.message}"
        }

        runOnUiThread {
            onResult(result)
        }
    }.start()
}