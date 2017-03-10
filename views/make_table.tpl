%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open project dependencies are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
<br>
<ul>
<li><a href="dependency/new">Add a new dependency</a>
<li><a href="dependency/json/all">Get the dependencies in JSON format</a>
</ul>
