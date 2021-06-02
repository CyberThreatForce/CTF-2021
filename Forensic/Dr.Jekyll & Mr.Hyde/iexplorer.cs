using System;
using System.Diagnostics;
using System.Threading;
namespace Explorer{
	class Program{
		static void Main(){
			Process.Start("c:\\Program Files\\Internet Explorer\\iexplore.exe", "https://www.youtube.com/watch?v=dQw4w9WgXcQ");
			Thread.Sleep("1500");
			Process proc = new Process();
			ProcessStartInfo procInfo = new ProcessStartInfo("powershell.exe");
			procInfo.CreateNoWindow = true;
			proc.StartInfo = procInfo;
			proc.Start();
		}
	}
}
