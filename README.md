<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module RAW2JPG</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>RAW2JPG</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/Users/josetorres/Desktop/github/RAW2JPG/RAW2JPG.py">/Users/josetorres/Desktop/github/RAW2JPG/RAW2JPG.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>

<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="RAW2JPG.html#RAW2JPG">RAW2JPG</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="RAW2JPG">class <strong>RAW2JPG</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>

<tr><td bgcolor="#ffc8d8"><tt>&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="RAW2JPG-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Initialize&nbsp;<a href="#RAW2JPG">RAW2JPG</a>&nbsp;<a href="builtins.html#object">object</a>&nbsp;and&nbsp;import&nbsp;all&nbsp;necessary&nbsp;libraries<br>
Dependencies:<br>
&nbsp;&nbsp;&nbsp;&nbsp;NumPy<br>
&nbsp;&nbsp;&nbsp;&nbsp;os<br>
&nbsp;&nbsp;&nbsp;&nbsp;time<br>
&nbsp;&nbsp;&nbsp;&nbsp;Image&nbsp;from&nbsp;PIL<br>
&nbsp;&nbsp;&nbsp;&nbsp;raw&nbsp;from&nbsp;rawkit<br>
Attributes:<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>queue</strong>&nbsp;=&gt;&nbsp;[]<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>raw_type</strong>&nbsp;=&gt;&nbsp;'.CR2'<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>jpgDir</strong>&nbsp;=&gt;&nbsp;None<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>listdir</strong>&nbsp;=&gt;&nbsp;os.listdir<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>mkdir</strong>&nbsp;=&gt;&nbsp;os.mkdir<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>path</strong>&nbsp;=&gt;&nbsp;os.path<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>utime</strong>&nbsp;=&gt;&nbsp;os.utime<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>array</strong>&nbsp;=&gt;&nbsp;np.array<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>Raw</strong>&nbsp;=&gt;&nbsp;raw.Raw<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>time</strong>&nbsp;=&gt;&nbsp;time.time<br>
&nbsp;&nbsp;&nbsp;&nbsp;self.<strong>frombytes</strong>&nbsp;=&gt;&nbsp;Image.frombytes</tt></dd></dl>

<dl><dt><a name="RAW2JPG-addOutputPath"><strong>addOutputPath</strong></a>(self, folder_path)</dt><dd><tt>Define&nbsp;the&nbsp;SINGLE,&nbsp;JPEG&nbsp;output&nbsp;folder&nbsp;path<br>
Input:<br>
&nbsp;&nbsp;&nbsp;&nbsp;folder_path<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None</tt></dd></dl>

<dl><dt><a name="RAW2JPG-addRawFile"><strong>addRawFile</strong></a>(self, file_path)</dt><dd><tt>Add&nbsp;a&nbsp;SINGLE,&nbsp;RAW&nbsp;file&nbsp;path&nbsp;to&nbsp;the&nbsp;internal&nbsp;queue<br>
Input:<br>
&nbsp;&nbsp;&nbsp;&nbsp;file_path<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None</tt></dd></dl>

<dl><dt><a name="RAW2JPG-addRawFolder"><strong>addRawFolder</strong></a>(self, folder_path)</dt><dd><tt>Add&nbsp;a&nbsp;SINGLE,&nbsp;RAW&nbsp;folder&nbsp;path&nbsp;to&nbsp;the&nbsp;internal&nbsp;queue<br>
Input:<br>
&nbsp;&nbsp;&nbsp;&nbsp;folder_path<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None</tt></dd></dl>

<dl><dt><a name="RAW2JPG-convertImages"><strong>convertImages</strong></a>(self)</dt><dd><tt>Initiate&nbsp;CR2&nbsp;to&nbsp;JPG&nbsp;conversion<br>
Input:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None</tt></dd></dl>

<dl><dt><a name="RAW2JPG-createFileSystem"><strong>createFileSystem</strong></a>(self)</dt><dd><tt>Create&nbsp;CR2/JPG&nbsp;folder&nbsp;system&nbsp;for&nbsp;easy&nbsp;Input/Output<br>
Input:<br>
&nbsp;&nbsp;&nbsp;&nbsp;None<br>
Output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;True&nbsp;(Bool)</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
</td></tr></table></td></tr></table>
</body></html>
