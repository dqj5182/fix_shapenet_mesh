def fix_shapenet_meshes(mesh_obj):
    points, face_indices = trimesh.sample.sample_surface(mesh_obj, 50000)
    cloud = pv.PolyData(points)
    mesh_obj_vol = cloud.delaunay_3d(alpha=2.)
    mesh_obj_shell = mesh_obj_vol.extract_geometry()
    vertices = np.array(mesh_obj_shell.points)
    faces = np.array(mesh_obj_shell.faces).reshape((-1, 4))[:, 1:]
    mesh_obj = trimesh.Trimesh(vertices, faces)
    return mesh_obj
